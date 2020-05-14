#!/usr/bin/env python
# coding: utf-8

# In[1]:


from qiskit import *
from numpy.random import randint
import numpy as np
print("Imports Successful")


# In[2]:


get_ipython().run_line_magic('matplotlib', 'inline')
from qiskit.tools.visualization import plot_histogram


# In[11]:


secretnumber = '0100'
n = 0000
alice_bases = randint(2, size =len(secretnumber))
print(alice_bases)


def encode_message(bits,bases):
    message = []
    for i in range(len(secretnumber)):
        qc = QuantumCircuit(1,1)
        if bases[i] == 0:
            if bits[i] == 0:
                pass
            else:
                qc.x(0)
        else:
            if bits[i] == 0:
                qc.h(0)
            else:
                qc.x(0)
                qc.h(0)
        qc.barrier()
        message.append(qc)
    return message 

message = encode_message(secretnumber, alice_bases)
print('basis = %i' % alice_bases[0])
message[2].draw()

bob_bases = randint(2, size = len(secretnumber))
print(bob_bases)


# 

# In[12]:


circuit = QuantumCircuit(len(secretnumber)+1, len(secretnumber))

#circuit.h([0,1,2,3,4,5])
circuit.h(range(len(secretnumber)))
circuit.x(len(secretnumber))
circuit.h(len(secretnumber))
circuit.barrier()

for ii, yesno in enumerate(reversed(secretnumber)):
    if yesno == '1':
        circuit.cx(ii, len(secretnumber))
#circuit.cx(5, 6)
#circuit.cx(3, 6)
#circuit.cx(0, 6)

circuit.barrier()
circuit.h(range(len(secretnumber)))
circuit.barrier()
#circuit.h([0,1,2,3,4,5])
circuit.measure(range(len(secretnumber)), range(len(secretnumber)))


# In[13]:


circuit.draw(output ='mpl')


# In[10]:


simulator = Aer.get_backend('qasm_simulator')
result = execute(circuit, backend=simulator, shots = 1).result()
counts = result.get_counts()
print(counts)


# In[ ]:




