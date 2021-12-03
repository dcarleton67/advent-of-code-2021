with open('Day 3/input.txt') as f:
    bitlines = f.readlines()

bitLength = len(bitlines[0])
def mostFrequent(List):
    return max(set(List), key = List.count)

mostCommonBits = [mostFrequent([bitline[i] for bitline in bitlines]) for i in range(bitLength - 1)]
leastCommonBits = ['1' if bit == '0' else '0' for bit in mostCommonBits]

gammaRate = ''.join(mostCommonBits)
epsilonRate = ''.join(leastCommonBits)
print(int(gammaRate, base=2)*(int(epsilonRate, base=2)))

oxygenGeneratorList = bitlines
co2ScrubberList = bitlines
for i in range(bitLength - 1):
    mostFrequentOxygenBit = 1
    for bitline in oxygenGeneratorList:
        if bitline[i] == '1': mostFrequentOxygenBit += 1
        else: mostFrequentOxygenBit -= 1
    if mostFrequentOxygenBit >= 1: mostFrequentOxygenBit = 1
    else: mostFrequentOxygenBit = 0

    mostFrequentCO2Bit = 1
    for bitline in co2ScrubberList:
        if bitline[i] == '1': mostFrequentCO2Bit += 1
        else: mostFrequentCO2Bit -= 1
    if mostFrequentCO2Bit >= 1: mostFrequentCO2Bit = 1
    else: mostFrequentCO2Bit = 0

    if len(oxygenGeneratorList) > 1:
        oxygenGeneratorList = list(filter(lambda bits: int(bits[i]) == mostFrequentOxygenBit, oxygenGeneratorList))
    if len(co2ScrubberList) > 1:   
        co2ScrubberList = list(filter(lambda bits: int(bits[i]) == (1 - mostFrequentCO2Bit), co2ScrubberList))

oxygenGenerator = oxygenGeneratorList[0]
co2Scrubber = co2ScrubberList[0]

print(int(oxygenGenerator, base=2)*(int(co2Scrubber, base=2)))