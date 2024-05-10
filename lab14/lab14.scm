(define (split-at lst n)
  (cond
    ((null? lst) (cons nil nil))
    ((= n 0) (cons nil lst))
    (else
        (define r (split-at (cdr lst) (- n 1)))
        (cons (cons (car lst) (car r)) (cdr r )
        )
    )
)
)


(define (compose-all funcs)
  (cond 
    ((null? funcs) (lambda (x) x))
     (else 
        (define g (compose-all (cdr funcs)))
        (lambda (x) (g ((car funcs) x)) )
        )
    )
)

