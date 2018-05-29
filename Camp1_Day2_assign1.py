"""
Cisco Black Belt: programability Level 1
Script to calculate number of session taken (dictionary, String manipulation)
submitted by: Vaibhav Solanki(vaibhav.solanki@agcnetworks.com)
"""
Sessions_Attended = {'sessions' : '1011,2344,3222,44322,555,6332,721,8789,99,1011,1124,1245,137,1499'}
session_list = Sessions_Attended['sessions'].split(',')
no_of_sessions = int((len(list((filter(bool, session_list))))))
print('I have attended {} sessions!!'.format(no_of_sessions))