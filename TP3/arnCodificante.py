from pampy import match, _

def parceAminoAcidChain(chain):
    a = ''
    for x in chain:
        a = a + parceAminoAcid(parceCodeOfAminoAcid(x))
    return a

def parceAminoAcid(aminoAcid):
    return match(aminoAcid,
        'His', 'CAU',
        'Arg', 'CGU',
        'Lys', 'AAA',
        'Ile', 'AUU',
        'Phe', 'UUU',
        'Leu', 'UUA',
        'Trp', 'UGG',
        'Ala', 'GCU',
        'Met', 'AUG',
        'Pro', 'CCU',
        'Cys', 'UGU',
        'Asn', 'AAU',
        'Val', 'GUU',
        'Gly', 'GGU',
        'Ser', 'UCU',
        'Gln', 'CAA',
        'Tyr', 'UAU',
        'Asp', 'GAU',
        'Glu', 'GAA',
        'Thr', 'ACU',
        _, 'None',
    )


def parceCodeOfAminoAcid(codeAminoAcid):
    return match(codeAminoAcid,
        'H', 'His',
        'R', 'Arg',
        'K', 'Lys',
        'I', 'Ile',
        'F', 'Phe',
        'L', 'Leu',
        'W', 'Trp',
        'A', 'Ala',
        'M', 'Met',
        'P', 'Pro',
        'C', 'Cys',
        'N', 'Asn',
        'V', 'Val',
        'G', 'Gly',
        'S', 'Ser',
        'Q', 'Gln',
        'Y', 'Tyr',
        'D', 'Asp',
        'E', 'Glu',
        'T', 'Thr',
        _, 'None'
    )

