# Youtube Unique Viewers (live stream)

viewers = set()


viewers.add("User1")
viewers.add("User2")
viewers.add("User1")    # rewatch ignored

print("Unique viewers: ", len(viewers))

# Shows real audience count correctly