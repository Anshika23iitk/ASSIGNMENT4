1. Initialize weights \( W^{[l]} \) and biases \( b^{[l]} \) randomly for all layers.

2. For each training example:
   a. **Forward Pass**:
      i. For each layer \( l = 1 \) to \( L \):
         - Compute \( z^{[l]} = W^{[l]}a^{[l-1]} + b^{[l]} \)
         - Compute \( a^{[l]} = g(z^{[l]}) \)

   b. **Backward Pass**:
      i. Compute output layer error:
         \( \delta^{[L]} = \frac{\partial J}{\partial a^{[L]}} \cdot g'(z^{[L]}) \)
      ii. For each layer \( l = L-1 \) to \( 1 \):
         - Compute \( \delta^{[l]} = (W^{[l+1]})^\top \delta^{[l+1]} \cdot g'(z^{[l]}) \)
         - Compute gradients:
           \( \frac{\partial J}{\partial W^{[l]}} = \delta^{[l]}(a^{[l-1]})^\top \)
           \( \frac{\partial J}{\partial b^{[l]}} = \delta^{[l]} \)

   c. **Update Weights and Biases**:
      i. For each layer \( l = 1 \) to \( L \):
         - \( W^{[l]} = W^{[l]} - \eta \frac{\partial J}{\partial W^{[l]}} \)
         - \( b^{[l]} = b^{[l]} - \eta \frac{\partial J}{\partial b^{[l]}} \)




