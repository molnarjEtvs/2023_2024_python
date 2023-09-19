
henrikValasz = input("Henrik jön e kosarazni? ")
hannaValasz = input("Hanna jön e kosarazni?")

if henrikValasz == "igen" and hannaValasz == "igen":
    print("Mind 2en jönnek")
elif henrikValasz == "nem" and hannaValasz =="nem":
    print("Egyik sem jön")
else:
    print("Egy jön csak")