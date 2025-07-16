#!/usr/bin/env python3
"""
Module generate_invitations
"""


def generate_invitations(template, attendees):
    """
    Generates personalized invitation files from a template
    """

    if not isinstance(template, str):
        print("Invalid input type: {}".format(type(template)))
        return    
    if not isinstance(attendees, list):
        print("Invalid input type: {}".format(type(attendees)))
        return
    else:
        for i in range(len(attendees)):
            if not isinstance(attendees[i], dict):
                print("Invalid input type: {}".format(type(attendees[i])))
                return

    if not template or template == "":
        print('Template is empty, no output files generated.')
        return

    if not attendees or attendees == []:
        print('No data provided, no output files generated.')
        return

    replace_fields = ['name', 'event_title', 'event_date', 'event_location']

    for i in range(len(attendees)):
        try:
            filename = 'output_{}.txt'.format(i + 1)
            with open(filename, 'w') as file:
                invitation = template
                for j in range(len(replace_fields)):
                    placeholder = "{" + replace_fields[j] + "}"
                    if attendees[i][replace_fields[j]] is None:
                        if replace_fields[j] == "event_date":
                            invitation = invitation.replace(
                                placeholder, "event_date:N/A")
                        else:
                            invitation = invitation.replace(placeholder, "N/A")
                    else:
                        invitation = invitation.replace(
                            placeholder, attendees[i][replace_fields[j]])
                file.write(invitation)
        except Exception as e:
            print("Error generating invitation for attendee\
                   #{}: {}".format(i + 1, e))
