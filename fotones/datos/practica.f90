

        program divisor
        use GetFiles
        implicit none

        integer ::i, a1, a2, a3, a4, a5, x, l, p_size
        character(len=35) :: nombre
        character(len=35), allocatable, dimension(:) ::archivos
        integer ::  cuentas = 20
        common cuentas
        real :: promedio
        real, allocatable, dimension(:) :: p

	integer :: k
	real :: c0_90, c90_0, c45_m45, cm45_45, BE

	open(5, file="base_datos.dat")
 
        call get_names (archivos)
        p_size = size(archivos)
        allocate(p(1:p_size))
!      call imprimir_nombres (archivos)

        do l = 1, p_size
          p(l) = promedio(archivos(l))
	  print*, l, p(l)
	  write(5,*) p(l)
        end do

	if (p_size  /= 4)  then 
		print*,("...upsis!") 
	else if (p_size == 4) then
		c0_90 = p(1)
		c90_0 = p(3)
		c45_m45 = p(2)
		cm45_45 = p(4)

		BE =  (p(2) + p(4)) /(p(1) + p(3))
		print*, "BE: " , BE
 
	end if

		

	close(5)

	

      end program divisor

      function promedio (archivo) result(prom)
        character(len=35), intent(in) :: archivo
        real                          :: prom
        integer ::i, a1, a2, a3, a4, a5, x, cont
        integer :: cuentas
        common cuentas
        open(unit=3, file=archivo)
        read(3,*)

        x = 0
        cont = 1
        do i = 1, cuentas
                read(3,*,end=11) a1, a2, a3, a4, a5
                x = x + a5
                cont = cont + 1
!               print *, i, a5
!               print*, x
11      end do
        prom = real(x) / cont
 !      print*, "Archivo: ", archivo,  "Promedio: ", prom
        close(3)

      end function promedio
