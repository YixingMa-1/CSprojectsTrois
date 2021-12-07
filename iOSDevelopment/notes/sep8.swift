func printName(firstName first:String, lastName last:String) {
    print("\(last), \(first)")
}

printName(first:"Hermione", last:"Granger")
// Argument
//      argemental internalName: type

// Argument labels
// - used when you CALL the function 
// - internal name is used when you IMPLEMENT the function 

func returnGreeting(personName: String) -> String {
    let newGreeting = "Hello, \(personName)!"
    return newGreeting
}

print(returnGreeting(personName:"Ron Wesley")) 

func minAndMax(myArray: [Int]) -> (min: Int,max: Int)) {
    var currentMax = myArray[0]
    var currentMin = myArray[0]
    // interate through the index
    for value in myArray[1 ..< myArray.count] {
        if value > currentMax {
            currentMax = Value
        } else if value < currentMin {
            currentMin = value
        }
    }
    return (currentMin, currentMax)
}

let extremes = minAndMax(myArray:[3, 65, 4, 9, 2, 7])
print(extremes)
// for tuples we use dot
print("min is: \(extremes.1)")

for index in 1.. < myArray.count {
    if myArray[index] > currentMax { 
        ...
    }
}