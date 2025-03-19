% Facts: Disease Symptoms and Factors
symptom(fever).
symptom(cough).
symptom(fatigue).
symptom(shortness_of_breath).

factor(infection).
factor(virus).
factor(bacteria).

% Rules for disease diagnosis
rule(flu, [fever, cough, fatigue, virus]).
rule(covid19, [fever, cough, shortness_of_breath, virus]).
rule(pneumonia, [fever, cough, shortness_of_breath, bacteria]).

% Forward Chaining Algorithm
forward_chain :-
    findall(Disease, (rule(Disease, Conditions), check_conditions(Conditions)), Diseases),
    write('Possible Diagnoses: '), nl,
    print_diseases(Diseases).

% Check if all conditions for a rule are met
check_conditions([]).
check_conditions([H|T]) :-
    (symptom(H); factor(H)),
    check_conditions(T).

% Print diagnosed diseases
print_diseases([]).
print_diseases([H|T]) :-
    write(H), nl,
    assert(factor(H)),  % Add new disease factor to knowledge base
    print_diseases(T).

% Query
:- forward_chain.
