!Trabalho de Analise Numerica
!Aluno: Jeferson R. Moura Moreira
!06-10-2011
!Implementar o metódo de Gauss-Legender para integrar uma função

!	Subrotina para calcular pesos e abscissas

subroutine PesAbsGL( T, A, n )

	double precision, intent(out) :: T(100), A(100)
	double precision p1, p2, p3, z, z1, pp, pi
	integer, intent(in) :: n
	integer m, i, j

	pi = 3.14159265358979323846
	m = (0.5*(n+1))

	do i = 1, m, 1
		z = cos(pi*(i-0.25)/(n+0.5))
		do while(.true.)
			p1 = 1
			p2 = 0
			do j = 1, n, 1
				p3 = p2
				p2 = p1
				p1 = ((2*j-1)*z*p2-(j-1)*p3)/j
			enddo
			pp = (n*((z*p1)-p2))/((z**2)-1)
			z1 = z
			z = z1-(p1/pp)

			if( abs(z-z1) .le. 10**(-15) ) then
			go to 22

			endif

		enddo

22 continue
		T(m+1-i) = z
		A(m+1-i) = 2/((1-z**2)*pp**2)
	enddo

end

double precision function funcao( x )
	double precision, intent(in) :: x
	funcao = x * sin(3*x)
end

!	Programa principal do metódo de Gauss-Legender

program GaussLegender

	double precision Tvet(100), Avet(100), integral, x, y
	double precision e1, e2, c1, c2, t1, c, b1, b2
	integer condErro, n, i, k

	read *, b1, b2, n

	if( n.lt.1 ) then
		condErro = 1
		return
	endif

	condErro = 0
	integral = 0
	
	call PesAbsGL( Tvet, Avet, n )
	e1 = ( b2 - b1 )/2
	e2 = ( b1 + b2 )/2

	if( mod(n,2).eq.0 ) then
		c1 = 1
		c2 = 0.5
	else
		c1 = 0
		c2 = 1
	endif

	do i = 1, n, 1

		k = int( i - 0.5 * (n+1) + sign( 1, int(i - 0.5 * (n+c1)) ) * c2 )
		t1 = sign( 1, k ) * Tvet( abs(k) )
		x = e1 * t1 + e2
		y = funcao( x )
		c = Avet( abs(k) )
		integral = integral + y * c

		write(*, 17) i, t1, x, y, c
17 format( i2, 4f10.5 )

	enddo

	integral = e1 * integral

	write(*, 16) integral, condErro
16 format(f15.10, i2)

end

