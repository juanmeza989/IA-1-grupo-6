(define (problem ProblemaEncargo)
  (:domain MundoRobot)

  (:objects
    robot cafe carta - object
    caja - contenedor
    oficina tienda buzon - lugar
  )

  (:init
    (en robot oficina)
    (en caja oficina)
    (en cafe tienda)
    (en carta buzon)
    (vacio)
  )

  (:goal
    (and
      (en robot oficina)
      (tiene cafe caja)
      (tiene carta caja)
      (sosteniendo-caja)
    )
  )
)