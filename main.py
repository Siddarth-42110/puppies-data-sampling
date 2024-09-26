import numpy as np

np.random.seed(42)
puppies = np.array([1,0,1,1,1,1,0,0,0,0,1,1,1,1,1,1,1,1,1,1])

p=puppies.mean()
print("mean:", p)
print("standard deviation", puppies.std())
print("variance", puppies.var())

np.random.choice(puppies, size=(1,5), replace=True)
np.random.choice(puppies, size=(1,5), replace=True).mean()

print("\nsampling distribution with size 5 \n")
sample_props=[]
for i in range(10000):
    sample = np.random.choice(puppies,5,replace=True)
    sample_props.append(sample.mean())
sample_props = np.array(sample_props)

sm = sample_props.mean()
print("mean", sample_props.mean())
print("standard deviation", sample_props.std())
print("variance", sample_props.var())

print("\nsampling distribution with size 20 \n")
twenty_sample_props=[]
for i in range(10000):
    sample = np.random.choice(puppies,20,replace=True)
    twenty_sample_props.append(sample.mean())
twenty_sample_props = np.array(twenty_sample_props)

sm = sample_props.mean()
print("mean", twenty_sample_props.mean())
print("standard deviation", twenty_sample_props.std())
print("variance", twenty_sample_props.var())