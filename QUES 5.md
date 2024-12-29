Let’s derive the backpropagation algorithm for a neural network with 
𝐾
K hidden layers, one input layer, and one output layer. Backpropagation involves two main steps: forward pass to calculate outputs and errors, and backward pass to compute gradients for updating weights. Below is the step-by-step derivation, followed by the pseudocode.

1. Notation
𝐿
L: Total number of layers (including input and output).
𝑧
[
𝑙
]
z 
[l]
 : Weighted sum of inputs for layer 
𝑙
l.
𝑎
[
𝑙
]
a 
[l]
 : Activation output of layer 
𝑙
l.
𝑊
[
𝑙
]
W 
[l]
 : Weights connecting layer 
𝑙
−
1
l−1 to 
𝑙
l.
𝑏
[
𝑙
]
b 
[l]
 : Biases for layer 
𝑙
l.
𝛿
[
𝑙
]
δ 
[l]
 : Error term (gradient of loss with respect to 
𝑧
[
𝑙
]
z 
[l]
 ).
𝑔
′
g 
′
 : Derivative of activation function.
𝐽
J: Loss function.
2. Forward Pass
For each layer 
𝑙
=
1
,
2
,
…
,
𝐿
l=1,2,…,L:

Compute the weighted sum:
𝑧
[
𝑙
]
=
𝑊
[
𝑙
]
𝑎
[
𝑙
−
1
]
+
𝑏
[
𝑙
]
z 
[l]
 =W 
[l]
 a 
[l−1]
 +b 
[l]
 
Apply activation function:
𝑎
[
𝑙
]
=
𝑔
(
𝑧
[
𝑙
]
)
a 
[l]
 =g(z 
[l]
 )
3. Backward Pass
Step 1: Compute Output Layer Error (
𝑙
=
𝐿
l=L)
For the output layer:

𝛿
[
𝐿
]
=
∂
𝐽
∂
𝑎
[
𝐿
]
⋅
𝑔
′
(
𝑧
[
𝐿
]
)
δ 
[L]
 = 
∂a 
[L]
 
∂J
​
 ⋅g 
′
 (z 
[L]
 )
Step 2: Backpropagate Error to Hidden Layers (
𝑙
=
𝐿
−
1
,
𝐿
−
2
,
…
,
1
l=L−1,L−2,…,1)
For each hidden layer 
𝑙
l:

𝛿
[
𝑙
]
=
(
𝑊
[
𝑙
+
1
]
)
⊤
𝛿
[
𝑙
+
1
]
⋅
𝑔
′
(
𝑧
[
𝑙
]
)
δ 
[l]
 =(W 
[l+1]
 ) 
⊤
 δ 
[l+1]
 ⋅g 
′
 (z 
[l]
 )
Step 3: Compute Gradients
For each layer 
𝑙
=
1
,
2
,
…
,
𝐿
l=1,2,…,L:

Gradients of weights:
∂
𝐽
∂
𝑊
[
𝑙
]
=
𝛿
[
𝑙
]
(
𝑎
[
𝑙
−
1
]
)
⊤
∂W 
[l]
 
∂J
​
 =δ 
[l]
 (a 
[l−1]
 ) 
⊤
 
Gradients of biases:
∂
𝐽
∂
𝑏
[
𝑙
]
=
𝛿
[
𝑙
]
∂b 
[l]
 
∂J
​
 =δ 
[l]
 
4. Update Weights and Biases
Using gradient descent, update weights and biases:

𝑊
[
𝑙
]
=
𝑊
[
𝑙
]
−
𝜂
∂
𝐽
∂
𝑊
[
𝑙
]
W 
[l]
 =W 
[l]
 −η 
∂W 
[l]
 
∂J
​
 
𝑏
[
𝑙
]
=
𝑏
[
𝑙
]
−
𝜂
∂
𝐽
∂
𝑏
[
𝑙
]
b 
[l]
 =b 
[l]
 −η 
∂b 
[l]
 
∂J
​
 
where 
𝜂
η is the learning rate.
