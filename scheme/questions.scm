(define (caar x) (car (car x)))
(define (cadr x) (car (cdr x)))
(define (cdar x) (cdr (car x)))
(define (cddr x) (cdr (cdr x)))

; Some utility functions that you may find useful to implement

(define (zip pairs)
    (cond 
        ((null? pairs) (list pairs pairs))   
        (else
            (define t (zip (cdr pairs)))
            (cons (cons (car (car pairs)) (car t)) (list (cons (car (cdr (car pairs))) (car (cdr t)))))
        )
    )
)


;; Problem 15
;; Returns a list of two-element lists



(define (helper s ind)
    (cond
        ((null? s) s)
        (else (cons (list ind (car s)) (helper (cdr s) (+ ind 1))))
        )
)


(define (enumerate s)
  ; BEGIN PROBLEM 15
  (helper s 0)
)
  ; END PROBLEM 15
(enumerate '(3 4 5 6))
;; Problem 16

;; Merge two lists LIST1 and LIST2 according to COMP and return
;; the merged lists.
(define (merge comp list1 list2)
  ; BEGIN PROBLEM 16
    (cond
        ((null? list1) list2)
        ((null? list2) list1)
        ((comp (car list1) (car list2)) (cons (car list1) (merge comp (cdr list1) list2)))
        (else (cons (car list2) (merge comp list1 (cdr list2))))
    )
  )
  ; END PROBLEM 16


(merge < '(1 5 7 9) '(4 8 10))
; expect (1 4 5 7 8 9 10)
(merge > '(9 7 5 1) '(10 8 4 3))
; expect (10 9 8 7 5 4 3 1)

;; Problem 17

(define (nondecreaselist s)
    ; BEGIN PROBLEM 17
    (cond 
        ((null? s) s)
        ((null? (cdr s)) (list (list (car s))))
        (else (define t (nondecreaselist (cdr s)))
            (if (> (car s) (car (car t))) (cons (list (car s)) t) (cons (cons (car s)(car t))(cdr t)))
        )
        
    )
)
(nondecreaselist '(1 2 3 4 1 2 3 4 1 1 1 2 1 1 0 4 3 2 1))
    ; END PROBLEM 17

;; Problem EC
;; Returns a function that checks if an expression is the special form FORM
(define (check-special form)
  (lambda (expr) (equal? form (car expr))))

(define lambda? (check-special 'lambda))
(define define? (check-special 'define))
(define quoted? (check-special 'quote))
(define let?    (check-special 'let))

;; Converts all let special forms in EXPR into equivalent forms using lambda
(define (let-to-lambda expr)
  (cond ((atom? expr)
         ; BEGIN PROBLEM EC
         expr
         ; END PROBLEM EC
         )
        ((quoted? expr)
         ; BEGIN PROBLEM EC
         expr
         ; END PROBLEM EC
         )
        ((or (lambda? expr)
             (define? expr))
         (let ((form   (car expr))
               (params (cadr expr))
               (body   (cddr expr)))
           ; BEGIN PROBLEM EC
           (define rbody (map let-to-lambda body))
           (cons 'lambda (cons params rbody))
           ; END PROBLEM EC
           ))
        ((let? expr)
         (let ((values (cadr expr))
               (body   (cddr expr)))
           ; BEGIN PROBLEM EC
           (define z (zip values))
           (define rbody (map let-to-lambda body))
           (define q (cons 'lambda (cons (car z) rbody)))
           (cons q (map let-to-lambda (car (cdr z))))
           ; END PROBLEM EC
           ))
        (else
         ; BEGIN PROBLEM EC
            (map let-to-lambda expr)
         ; END PROBLEM EC
         )))

