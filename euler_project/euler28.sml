fun calc(Y) = if(0 = (Y mod 2)) then 3*IntInf.pow(Y,2)+3 else IntInf.pow(Y,2)

fun diagonal (1) = 1
	| diagonal (X) =
		let
			val a = diagonal(X-1)
			val b = calc(X)
			val c = a + b
		in
			c
		end

