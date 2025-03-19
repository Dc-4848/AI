% Define heuristic values for each node.
heuristic(a, 10).
heuristic(b, 8).
heuristic(c, 5).
heuristic(d, 7).
heuristic(e, 3).
heuristic(f, 0).

% Define graph edges with cost.
graph(a, b, 4).
graph(a, c, 3).
graph(b, d, 5).
graph(c, e, 7).
graph(d, f, 4).
graph(e, f, 2).

% Best First Search Algorithm with Cost Calculation
best_first_search(Start, Goal, Path, Cost) :-
    best_first_search_helper([(Start, [Start], 0)], Goal, [], Path, Cost).

% Helper function: Expands nodes based on heuristic values.
best_first_search_helper([(Goal, Path, Cost)|_], Goal, _, Path, Cost) :- !.

best_first_search_helper([(Current, Path, CurrCost)|Rest], Goal, Visited, FinalPath, FinalCost) :-
    findall((Next, [Next|Path], NewCost), 
        (graph(Current, Next, EdgeCost), \+ member(Next, Visited), NewCost is CurrCost + EdgeCost), 
        Neighbors),
    manual_sort_by_heuristic(Neighbors, SortedNeighbors),
    append(SortedNeighbors, Rest, NewQueue),
    best_first_search_helper(NewQueue, Goal, [Current|Visited], FinalPath, FinalCost).

% Manual sorting of neighbors based on heuristic values (Bubble Sort implementation)
manual_sort_by_heuristic(List, Sorted) :-
    bubble_sort(List, Sorted).

bubble_sort(List, Sorted) :-
    swap(List, List1), !, 
    bubble_sort(List1, Sorted).
bubble_sort(Sorted, Sorted).

swap([(N1, P1, C1), (N2, P2, C2) | T], [(N2, P2, C2), (N1, P1, C1) | T]) :-
    heuristic(N1, H1),
    heuristic(N2, H2),
    H1 > H2.
swap([X | T], [X | T1]) :- 
    swap(T, T1).