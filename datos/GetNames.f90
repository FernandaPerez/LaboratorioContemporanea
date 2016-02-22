        module GetFiles

        contains
        subroutine get_names (nombres)
                
                character(len=35), dimension(:),allocatable,intent(out) :: nombres
                integer :: lines,j
                character(len=30) :: path
                character(len=60) :: cmd

                open (unit=2, file="data.txt")

                read(2,*) lines
                print*, lines

                allocate (nombres (1:lines))

                do j = 1, lines
                        read(2,*) nombres(j)
!                       print*, nombres(j)
                end do

                close(2)
!               print*, size(nombres)
!               call system('rm data.txt')
                return
        end subroutine get_names

        subroutine imprimir_nombres  (arreglo)
          integer :: a, k
          character(len=35), allocatable, dimension(:), intent(in) :: arreglo
          a = size(arreglo)

          do k = 1, a
            print*, k, " ",arreglo(k)
          end do

        end subroutine imprimir_nombres

        end module
