import storage

# rename CIRCUITPY drive

new_name = "Macropad"
storage.remount("/", readonly=False)
m = storage.getmount("/")
m.label = new_name
storage.remount("/", readonly=True)
