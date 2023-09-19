
hannaValasz = input("Hanna jön e kosarazni?")
henrikValasz = input("Henrik jön e kosarazni?")

if hannaValasz == "igen" and henrikValasz == "igen":
    print("Minde ketten jönnek")
elif hannaValasz == "nem" and henrikValasz == "nem":
    print("Egyik sem jön")
else:
    print("Egyikük jön csak")