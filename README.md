# Error-Tolerant L23 QKD protocol (ET-23) implementation.

This repository contains a Qiskit implementation of two different Frame-Based Reconciliation Quantum Key Distribution protocols:
* _Pure L23_: Implementation of Lizama et al. article: _Reverse Reconciliation for Optimal Error Correction in Quantum Key Distribution_, without the _Auxiliary Algorithm 2_ for error correction [1].
* _Error-Tolerant L23_: Implementation of an Error-Tolerant version of L23 [2].

## Success probability of L23

Alice sends randomly distributed quantum states $|0\rangle$, $|1\rangle$, $|+\rangle$ and $|-\rangle$. Bob groups each pair that collapses to the same bit and constructs lists $L_1$ and $L_2$. Alice searchs for elements $f_1, f_5 \in L_1$ that have the following structure:
```math
f_1 = \begin{pmatrix} |+\rangle & |1\rangle \\ |-\rangle & |0\rangle \end{pmatrix} , f_5 = \begin{pmatrix} |-\rangle & |0\rangle \\ |+\rangle & |1\rangle \end{pmatrix}
```

Finding these specific frames comes to a drawback: there is a probability that the protocol fails because Alice could not find them. Then, we define the success probability as the probability of find at least one $f_1$ or $f_5$ frame, so Alice can recover the secret key successfully. The following table presents the results, without the presence of errors:

| Qubits | Success probability |
|:------:|:-------------------:|
| 8      | 2,719%              |
| 16     | 28.494%             |
| 32     | 83,643%             |


## Tolerability of L23

We implement an error-tolerant version of L23, where error correction methods are not used. Instead, Alice searchs for half frames $f'_1$ and $f'_5$:

```math
f'_1 = \begin{pmatrix} |+\rangle & |1\rangle \\ ? & ?  \end{pmatrix} = \begin{pmatrix} ? & ? \\ |-\rangle & |0\rangle \end{pmatrix}
```

```math
f'_5 = \begin{pmatrix} |-\rangle & |0\rangle \\ ? & ? \end{pmatrix}  = \begin{pmatrix} ? & ? \\ |+\rangle & |1\rangle \end{pmatrix}
```

where "$?$" symbol means a random quantum state. Then, Alice computes all the possible secret keys, and if one of them is the same as Bob's, the QKD instance tolerates the error, assuming depolarization errors.

| Depolarizing probability | Tolerability |
|:------------------------:|:------------:|
| 10%                      | 98%          |
| 20%                      | 97%          |
| 30%                      | 95%          |
| 40%                      | 94%          |
| 50%                      | 92%          |
| 60%                      | 91%          |
| 70%                      | 88%          |
| 80%                      | 85%          |
| 90%                      | 81%          |
| 100%                     | 75%          |

## References
[1] Luis Adrian Lizama-Perez. Reverse reconciliation for optimal error correction in quantum key distribution. Symmetry, 15(3), 2023.  
[2] Submitted to IEEE Quantum Week 2024.
