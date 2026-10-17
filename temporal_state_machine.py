
"""
Temporal smoothing, confirmation and reset logic.
Layer: State Machine
"""

from __future__ import annotations
from dataclasses import dataclass


@dataclass
class StateTransition:
    confirmed_fall: bool
    reset_fall: bool
    active_fall: bool
    event_type: str | None = None


class TemporalStateMachine:
    def __init__(self):
        self.confirm_frames = 8
        self.reset_frames = 20

    def update(self, state, score_result, now_t=None):
        state.setdefault("candidate_frames", 0)
        state.setdefault("dynamic_frames", 0)
        state.setdefault("normal_frames", 0)
        state.setdefault("fall_detected", False)
        state.setdefault("fall_confirmed_time", None)
        state.setdefault("fall_reset_time", None)

        signals = score_result.signal_scores

        # Look for movement associated with a possible fall.
        dynamic_signal = (
            signals.get("velocity", 0) > 0.20
            or signals.get("height_drop", 0) > 0.25
            or signals.get("head_vel", 0) > 0.25
            or signals.get("collapse", 0) > 0.30
            or signals.get("ang_vel", 0) > 0.20
        )

        if score_result.candidate:
            state["candidate_frames"] += 1
            state["normal_frames"] = 0

            if dynamic_signal:
                state["dynamic_frames"] += 1
            else:
                state["dynamic_frames"] = 0
        else:
            state["normal_frames"] += 1
            state["candidate_frames"] = 0
            state["dynamic_frames"] = 0

        confirmed = False

        # Confirm only after sustained candidate frames and
        # evidence of fall-like movement. No instant high-score bypass.
        if (
            state["candidate_frames"] >= self.confirm_frames
            and state["dynamic_frames"] >= 2
            and score_result.signal_scores.get("velocity", 0) > 0.20
            and (
                score_result.signal_scores.get("height_drop", 0) > 0.25
                or score_result.signal_scores.get("head_vel", 0) > 0.25
                or score_result.signal_scores.get("collapse", 0) > 0.30
                )
            ):
            if not state["fall_detected"]:
                confirmed = True
                state["fall_confirmed_time"] = now_t

            state["fall_detected"] = True

        # Reset after sustained normal frames or clear upright posture.
        ar = state.get("aspect_ratio", 1.0)
        angle = state.get("torso_angle", 90.0)

        standard_reset = state["normal_frames"] >= self.reset_frames
        clearly_upright = ar < 0.35 and angle < 18.0
        geometry_reset = (
            clearly_upright and state["normal_frames"] >= 5
        )

        reset = (
            state["fall_detected"]
            and (standard_reset or geometry_reset)
        )

        if reset:
            state["fall_detected"] = False
            state["candidate_frames"] = 0
            state["dynamic_frames"] = 0
            state["fall_reset_time"] = now_t

        return StateTransition(
            confirmed_fall=confirmed,
            reset_fall=reset,
            active_fall=state["fall_detected"],
        )
