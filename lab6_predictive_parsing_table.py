
table = {
('E','i'):'E->TR',
('E','('):'E->TR',

('R','+'):'R->+TR',
('R',')'):'R->ε',
('R','$'):'R->ε',

('T','i'):'T->FY',
('T','('):'T->FY',

('Y','*'):'Y->*FY',
('Y','+'):'Y->ε',
('Y',')'):'Y->ε',
('Y','$'):'Y->ε',

('F','i'):'F->i',
('F','('):'F->(E)'
}

print("Predictive Parsing Table\n")

for k,v in table.items():
    print(k,"=>",v)
