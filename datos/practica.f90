

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


        call get_names (archivos)
        p_size = size(archivos)
        allocate(p(1:p_size))
!      call imprimir_nombres (archivos)

        do l = 1, p_size
          p(l) = promedio(archivos(l))
        end do



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
        print*, "Archivo: ", archivo,  "Promedio: ", prom
        close(3)

      end function promedio
