calc(A, W) :- ((0 is mod(A, 2)) -> W is 3*(A**2)+3; W is (A**2)).

diagonal(1, 1).
diagonal(X, W) :- Y is X-1, diagonal(Y, Z), calc(X, K), W is Z + K.
