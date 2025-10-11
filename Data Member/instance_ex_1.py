class InstanceDataMember: pass

s1=InstanceDataMember()
s2=InstanceDataMember()
s1.sno=100
s2.sno=200
print(s1.sno)
print(s2.__dict__)