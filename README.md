# Weak Approximation for 0-cycles on a product of elliptic curves

This is the code relevant to the computations appear in the Appendix A of the paper *'Weak Approximation for 0-cycles on a product of elliptic curves'* by **Evaggelia Gazaki**. 
The computations were done in Sage by **Angelos Koutsianas**.

The main function is the *rank_one_elliptic_curves*, where the input is the range of the values of n. The function returns the values of n for which Sage 
was not able to determine the bound (*bounds_not_equal*), the values of n for which Sage was not able to determine a generator of the Mordell-Weil group
(*not_compute_gens*) and the values of n for which Sage is able to compute the Mordell-Weil group and either there exists a "good" rational point P or not 
(respectively *success*, *failure*).  
