import sys

bags=[[0.1,1.0,0],[0.2,0.75,0.25],[0.4,0.5,0.5],[0.2,0.25,0.75],[0.1,0,1.0]]
obs=0.5
bags_copy=[]

def find_posterior(candType):
    bags_copy=bags
    for b in bags_copy:
        if candType=='C':
            b[0]=b[1]*b[0]/obs
        else:
            b[0]=b[2]*b[0]/obs


def find_observation(candType):
    obs=0 
    for b in bags_copy:
        if candType=='C':
            obs=obs+[0]*b[1]
        else:
            obs=obs+b[0]*b[2]
    return obs


sequenceText=sys.argv[1]
file_obj=open('result.txt','w')
print('\n Observation sequence:',sequenceText)
file_obj.write('\n Observation sequence:{}'.format(sequenceText))
print(' Length of sequence:',len(sequenceText))
file_obj.write('\n Length of sequence:{}\n'.format(len(sequenceText)))
find_observation(sequenceText[0])
sequenceText=sequenceText+'C'
for i in range(len(sequenceText)-1):
    file_obj.write('\n After Observation {}: {}\n'.format(i+1,sequenceText[i]))
    print('\n After Observation {}: {}\n'.format(i+1,sequenceText[i]))
    find_posterior(sequenceText[i])
    curr_obs=find_observation(sequenceText[i+1])
    for j in range(len(bags)):
        file_obj.write("\n P(h{} | Q)={}".format(j+1,bags[j][0]))
        print("\n P(h{} | Q)={}".format(j+1,bags[j][0]))
    if sequenceText[i+1]=='C':
        file_obj.write('\n Probability that the next candy will be C,given Q:{}'.format(curr_obs))
        file_obj.write('\n Probability that the next candy will be L,given Q:{}\n'.format(1-curr_obs))
        print('\n Probability that the next candy will be C,given Q:{}'.format(curr_obs))
        print('\n Probability that the next candy will be L,given Q:{}'.format(1-curr_obs))
    else:
        file_obj.write('\n Probability that the next candy will be C,given Q:{}'.format(1-curr_obs))
        file_obj.write('\n Probability that the next candy will be L,given Q:{}\n'.format(curr_obs))
        print('\n Probability that the next candy will be C,given Q:{}'.format(1-curr_obs))
        print('\n Probability that the next candy will be L,given Q:{}'.format(curr_obs))
print(' ****** Results are available in result.txt file ******')
file_obj.close()