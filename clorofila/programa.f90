    program clorofila
    implicit none
    real:: t1, t2, t3, t4, t5, A1, A2, A3, A4, A5
    integer :: i, cont, l
    real absorbance

    open(2, file="Untitled.csv")
    open(3, file="resultados.dat")
    read(2,*)

    cont = 0
    do i=1,34
      read(2,*, END=10) l, t2, t3, t4, t5
      !print*, l, t2, t3, t4, t5

      A2 = absorbance(t2)
      A3 = absorbance(t3)
      A4 = absorbance(t4)
      A5 = absorbance(t5)

      print*, l, A2, A3, A4, A5
      write(3,*) l, A2, A3, A4, A5


      cont = cont + 1
    end do
10  print*, "Ups"




    end program

    function absorbance(T) result(A)
      real, intent(in):: T
      real            :: A

      A = 2.0 - log10(T)
    end function absorbance
