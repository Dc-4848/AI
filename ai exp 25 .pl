% Possible actions the monkey can take
move(state(middle, on_floor, middle, has_not), grasp, state(middle, on_box, middle, has)).

move(state(P, on_floor, P, H), climb, state(P, on_box, P, H)).
move(state(P1, on_floor, P1, H), push(P1, P2), state(P2, on_floor, P2, H)).
move(state(P1, on_floor, B, H), walk(P1, P2), state(P2, on_floor, B, H)).

% Goal state: Monkey has the banana
can_get(state(_, _, _, has)).
can_get(State1) :- move(State1, _, State2), can_get(State2).
