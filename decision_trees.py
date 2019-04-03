import fileinput
import math
    
class Node():
    def __init__(self):
        self.name = ""
        self.attributes = []
        self.position = 0
        
def calculateEntropy(nodes, data):
    entropy = 0
    count = {}
    relation = nodes[len(nodes)-1]
    total = len(data)
    
    #Inicializar variables 
    for attribute in relation.attributes:
        count[attribute] = 0
        
    for i in range(len(data)):
        max = len(data[i])-1
        attribute = data[i][max]
        
        count[attribute] += 1
        
    for attribute in count:
        entropy -= (count[attribute] / total) * (math.log(count[attribute] / total) / math.log(2))
            
    return entropy


def id3(nodes,entropy,data):
    
    
    return 1

    
def main():
    lines = []
    attributes = {}
    data = []
    nodes = [] 
    
    i=0
    for line in fileinput.input():
    
        if line[0] != '%':
            line = line.rstrip()
            lines.append(line)
            print(line)
            
            if line.startswith('@data') or line.startswith('@relation') or line == '':
                continue
            elif line.startswith('@attribute'):
                node = Node()
                attribute_values = line.replace(',', "").replace('{', "").replace('}', "").split()[1:]
                name = attribute_values[0]
                attributes[i] = attribute_values
                i=i+1
                
                node.name = name
                node.attributes = attribute_values[1:]
                node.position = i - 1
                
                relation = name
                
                nodes.append(node)
                
                #print(node.name)
                #print(node.attributes)
                #print(node.position)
                
            else: 
                line = line.split(',')
                data.append(line)
                

    #print(lines)
    #print(attributes)
    #print(relation)
    #print(data)
    
    entropy = calculateEntropy(nodes, data)
    print(entropy)
    tree = id3(nodes,entropy,data)

if __name__ == '__main__':
  main()
