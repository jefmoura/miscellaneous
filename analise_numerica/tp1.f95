!Trabalho de Análise Númerica
!Aluno: Jeferson R. Moura Moreira

program PesAbsGL
implicit none

	double precision z, z1, pp, pi
	double precision p1, p2, p3, T(100), A(100)
	integer n, m, condErro, i, j

	read *, n

	if( n.lt.1 ) then
		condErro = 1
		write(*,15) condErro
15 format(i2)
		return
	endif

	condErro = 0
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

			if(abs(z-z1) .le. 10**(-15)) then
			go to 22

			endif

		enddo

22 continue
		T(m+1-i) = z
		A(m+1-i) = 2/((1-z**2)*pp**2)
	enddo

	write(*,15) condErro

	do i = 1, m, 1
		write(*,16) i, A(i), T(i)
16 format(i2,2f10.5)
	enddo
end
