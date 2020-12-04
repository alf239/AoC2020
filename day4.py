
z = [s.replace('\n', ' ') for s in x.split('\n\n')]

def valid(p):
    fields = set([f.split(':')[0] for f in p.replace(' ', '\n').split('\n')])
    expected = set(['ecl', 'pid', 'eyr', 'hcl', 'byr', 'iyr', 'hgt'])
    return not expected.difference(fields)

def valid2(p):
    try:
        fields = dict([(f.split(':')[0], f.split(':')[1]) for f in p.replace(' ', '\n').split('\n')])
        # byr (Birth Year) - four digits; at least 1920 and at most 2002.
        byr = int(fields['byr'])
        if byr < 1920 or byr > 2002:
            print('wrong byr: ' + fields['byr'])
            return False
        # iyr (Issue Year) - four digits; at least 2010 and at most 2020.
        iyr = int(fields['iyr'])
        if iyr < 2010 or iyr > 2020:
            print('wrong iyr: ' + fields['iyr'])
            return False
        # eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
        eyr = int(fields['eyr'])
        if eyr < 2020 or eyr > 2030:
            print('wrong eyr: ' + fields['eyr'])
            return False
        # hgt (Height) - a number followed by either cm or in:
        hgt = fields['hgt']
        # If cm, the number must be at least 150 and at most 193.
        if hgt.endswith('cm'):
            h = int(hgt[:-2])
            if h < 150 or h > 193:
                print('wrong hgt: ' + fields['hgt'])
                return False
        # If in, the number must be at least 59 and at most 76.
        elif hgt.endswith('in'):
            h = int(hgt[:-2])
            if h < 59 or h > 76:
                print('wrong hgt: ' + fields['hgt'])
                return False
        else:
            print('wrong hgt: ' + fields['hgt'])
            return False
        # hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
        if not re.search('^\#[0-9a-f]{6}$', fields['hcl']):
            print('wrong hcl: ' + fields['hcl'])
            return False
        # ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
        if fields['ecl'] not in  set('amb blu brn gry grn hzl oth'.split(' ')):
            print('wrong ecl: ' + fields['ecl'])
            return False                                         
        # pid (Passport ID) - a nine-digit number, including leading zeroes.
        if not re.search('^[0-9]{9}$', fields['pid']):
            print('wrong pid: ' + fields['pid'])
            return False
        # cid (Country ID) - ignored, missing or not.
        return True
    except BaseException as e:
        print('Exception: ' + str(e))
        return False
    



