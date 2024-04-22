# Error-Tolerant L23 QKD protocol (ET-23) implementation.

This repository contains a Qiskit implementation of two different Frame-Based Reconciliation Quantum Key Distribution protocols:
* _Pure L23_: Implementation of Lizama et al. article: _Reverse Reconciliation for Optimal Error Correction in Quantum Key Distribution_, without the _Auxiliary Algorithm 2_ for error correction [1].
* _Error-Tolerant L23_: Implementation of an Error-Tolerant version of L23 [2].

## Success probability

Alice sends randomly distributed quantum states $|0\rangle$, $|1\rangle$, $|+\rangle$ and $|-\rangle$. Bob groups each pair that collapses to the same bit and constructs lists $L_1$ and $L_2$. Alice searchs for elements $f_1, f_5 \in L_1$ that have the following structure:
```math
f_1 = \begin{pmatrix} |+\rangle & |1\rangle \\ |-\rangle & |0\rangle \end{pmatrix} , f_5 = \begin{pmatrix} |-\rangle & |0\rangle \\ |+\rangle & |1\rangle \end{pmatrix}
```

Finding these specific frames comes to a drawback: there is a probability that the protocol fails because Alice could not find them. Using ET-L23, Alice searchs for elements $f'_1, f'_5 \in L_1$ such as:
```math
        f'_1 = \begin{pmatrix}
            |+\rangle & |1\rangle \\
            ? & ? 
            \end{pmatrix} = \begin{pmatrix}
            ? & ? \\
            |-\rangle & |0\rangle
            \end{pmatrix} ,
```

```math
        f'_5 = \begin{pmatrix}
            |-\rangle & |0\rangle \\
            ? & ?
            \end{pmatrix}  = \begin{pmatrix}
            ? & ? \\
            |+\rangle & |1\rangle
            \end{pmatrix} .
```

Then, we define the Success probability as the probability of find at least one $f_1$ ($f'_1$) or $f_5$ ($f'_5$) frame, so Alice can recover the secret key successfully. The following table presents the results, without the presence of errors:

| Qubits | L23 | ET-23 |
|:------:|:-------------------:|:------------:|
| 8      | 2,7%                | 26,7%        |
| 16     | 28.5%               | 87,2%        |
| 32     | 83,6%               | 99,9%        |


## Tolerability

We implement the first error-tolerant frame-based reconciliation quantum key distribution protocol using L23 frames and secret key generation rules. After searching for $f'_1$ and $f'_5$ frames, instead of using an error correction method as in L23, in ET-L23 we test all possible keys that can be generated with each pivot. If one of them is the same as Bob's, the QKD instance tolerantes the error, assuming depolarization errors.

We calculate the Tolerability as the probability of successfully obtaining the shared key in the presence of errors on the quantum channel without using error correction methods. We compare the error-tolerant capabilities of L23 and ET-L23, where the results are given below.

| Depolarizing probability | L23         |        ET-23  |
|:------------------------:|:------------:|:------------:|
| 10%                      | 97%          | 98,2%        |
| 20%                      | 90%          | 96,4%        |
| 30%                      | 80,1%        | 94,1%        |
| 40%                      | 71,1%        | 93,1%        |
| 50%                      | 62%          | 91,3%        |
| 60%                      | 52,5%        | 86,8%        |
| 70%                      | 45,2%        | 84,5%        |
| 80%                      | 38,2%        | 81,5%        |
| 90%                      | 29,6%        | 78,1%        |
| 100%                     | 23,5%        | 69,3%        |

## References
[1] Luis Adrian Lizama-Perez. Reverse reconciliation for optimal error correction in quantum key distribution. Symmetry, 15(3), 2023.  
[2] Submitted to IEEE Quantum Week 2024.
