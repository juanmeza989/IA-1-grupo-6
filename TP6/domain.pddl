(define (domain MundoRobot)
  (:requirements :strips :typing)
  
  (:types 
    lugar contenedor - object
  )

  (:predicates
    (en ?o - object ?l - lugar)
    (sosteniendo ?o - object)
    (sosteniendo-caja)
    (tiene ?o - object ?c - contenedor)
    (vacio)
  )

  (:action Ir
    :parameters (?lugar1 - lugar ?lugar2 - lugar)
    :precondition (en robot ?lugar1)
    :effect (and
      (not (en robot ?lugar1))
      (en robot ?lugar2)
    )
  )

  (:action Tomar
    :parameters (?o - object ?l - lugar)
    :precondition (and
      (en robot ?l)
      (en ?o ?l)
      (vacio)
    )
    :effect (and
      (not (en ?o ?l))
      (not (vacio))
      (sosteniendo ?o)
    )
  )

  (:action Dejar
    :parameters (?o - object ?l - lugar)
    :precondition (and
      (en robot ?l)
      (sosteniendo ?o)
    )
    :effect (and
      (not (sosteniendo ?o))
      (en ?o ?l)
      (vacio)
    )
  )
  
  (:action TomarCaja
    :parameters (?l - lugar)
    :precondition (and
      (en robot ?l)
      (en caja ?l)
      (vacio)
    )
    :effect (and
      (not (en caja ?l))
      (not (vacio))
      (sosteniendo-caja)
    )
  )
  
  (:action PonerEnCaja
    :parameters (?o - object ?l - lugar)
    :precondition (and
      (en robot ?l)
      (en ?o ?l)
      (sosteniendo-caja)
    )
    :effect (and
      (not (en ?o ?l))
      (tiene ?o caja)
    )
  )
)