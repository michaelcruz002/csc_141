import matplotlib.pyplot as plt  # type: ignore[reportMissingModuleSource]
squares = [1, 4, 9, 16, 25]
fig,ax = plt.subplots()
ax.plot(squares, linewidth=3)