          program Analisis

          implicit none
		  integer ::  N,i, Nframes, salto
		  real :: dat, dt,tiempo
                  character (len=20)::  nombre_archivo
                  character (len=20):: archivo_in

      print*, "Archivo a Analizar:"
      read(*,*) archivo_in

		  print*, "Nombre del archivo a crear"
                  read(*,*) nombre_archivo
		  open(unit=2, file=archivo_in, status='old')
                  open(unit=3, file=nombre_archivo, action='write',status="replace")

		  print*, "Numero de Cuadros"
          read(*,*) Nframes
		  print*, "Frames por salto (El numero de f debe ser divisible)"
		  read(*,*) salto
		  print*, "dt suministrado por Tracker"
		  read(*,*) dt

		  N = Nframes/salto
      tiempo = 360
		  do i=1,N
		     tiempo = tiempo + (dt*salto)
			 read(2,*) dat
			 write(3,*) tiempo, dat
             print*, tiempo, dat
			 end do

		   close(2)
		   close(3)

		  end program
