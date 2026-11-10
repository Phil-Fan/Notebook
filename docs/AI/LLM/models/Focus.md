# 重点问题讨论

## 残差连接

- 残差连接：通过将输入信号直接添加到输出信号中，可以有效地解决梯度消失问题，提高模型的训练速度和性能。

## Layer Norm

- GPT3：采用了 Post-Layer Normalization（后标准化）的结构，即先进行自注意力或前馈神经网络的计算，然后进行 Layer Normalization。这种结构有助于稳定训练过程，提高模型性能。
- LLAMA：采用了 Pre-Layer Normalization（前标准化）的结构，即先进行 Layer Normalization，然后进行自注意力或前馈神经网络的计算。这种结构有助于提高模型的泛化能力和鲁棒性。
- ChatGLM：采用了 Post-Layer Normalization 的结构，类似于 GPT3。这种结构可以提高模型的性能和稳定性。

## 激活函数

- ReLU（Rectified Linear Unit）：一种简单的激活函数，可以解决梯度消失问题，加快训练速度。
- GeLU（Gaussian Error Linear Unit）：一种改进的 ReLU 函数，可以提供更好的性能和泛化能力。
- Swish：一种自门控激活函数，可以提供非线性变换，并具有平滑和非单调的特性。



## 消融实验

- 消融实验：通过逐步移除模型中的某些组件或参数，观察模型性能的变化，从而确定模型中哪些组件或参数对模型性能的提升最为重要。
