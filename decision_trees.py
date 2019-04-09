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
        
    for i in range(total):
        max = len(data[i])-1
        attribute = data[i][max]
        
        count[attribute] += 1
        
    for attribute in count:
        if count[attribute] != 0:
            entropy -= (count[attribute] / total) * (math.log(count[attribute] / total) / math.log(2))
            
    return entropy
    
def calculateIG(nodes, data, name, entropy):
    info_gain = entropy
    for node in nodes:
        for attribute in node.attributes:
            if(node.name == name):
                split = [row for row in data if attribute == row[node.position]]
                info_gain -= ((len(split) / len(data)) * calculateEntropy(nodes, split))
    
    return info_gain

def id3(nodes,entropy,data,cont):
    if entropy == 0:
        print("  " * cont  + "ANSWER:"+ data[0][nodes[len(nodes)-1].position])
    else:
        best_ig = 0
        
        for node in nodes:
            if(node != nodes[len(nodes)-1]):
                calc_ig = calculateIG(nodes, data,node.name,entropy)
                if(calc_ig > best_ig):
                    best_ig = calc_ig
                    best_feature = node
        
        for attribute in best_feature.attributes:
            print("  " * cont + best_feature.name + ":" + attribute)
            split = [row for row in data if attribute == row[best_feature.position]]
            aux_entropy = calculateEntropy(nodes, split)
            
            if(len(split)>0):
                id3(nodes,aux_entropy,split, cont+1)

    
def main():
    lines = []
    attributes = {}
    data = []
    nodes = [] 
    cont = 0
    i=0
    
    
    for line in fileinput.input():
    
        if line[0] != '%':
            line = line.rstrip()
            lines.append(line)
            #print(line)
            
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
    
    id3(nodes,entropy,data,cont)

if __name__ == '__main__':
  main()
