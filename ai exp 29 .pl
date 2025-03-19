% Facts: Disease Symptoms and Factors
:- dynamic symptom/1, factor/1.  % Allow dynamic modification of symptoms and factors

symptom(fever).
symptom(cough).
symptom(fatigue).
symptom(shortness_of_breath).  % Added to ensure pneumonia can be diagnosed

factor(infection).
factor(virus).
factor(bacteria).

% Rules for disease diagnosis
rule(flu, [fever, cough, fatigue, virus]).
rule(covid19, [fever, cough, shortness_of_breath, virus]). % Added COVID-19 rule back
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
    assertz(factor(H)),  % Ensure the factor is dynamically added
    print_diseases(T).

% Query
:- forward_chain.
