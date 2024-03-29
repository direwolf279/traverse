''' This module will hold all string related functions, manipulation and/or operations '''


class StringHelper:
    ''' Main class for String Helper methods. '''
    @staticmethod
    def replace_email_domain(email, domain):
        ''' Pass in the email (original) and the domain you want instead (Not The Extension). This returns the updated email as a string. '''
        pos_a = email.index('@')
        pos_dot = email.rindex('.')
        return email.replace(email[pos_a:pos_dot], domain)


    @staticmethod
    def convert_to_csv(list_items, add_single_quotes=False, seperator=','):
        ''' Pass in a list and you will be returned a csv string. '''
        if isinstance(list_items, list):
            csv = f'{seperator}'.join(map(str, list_items))
            if add_single_quotes is True:
                csv = str(list_items)
                csv = csv.replace('[', '').replace(']', '')
            return csv


    @staticmethod
    def add_chars_to_list_items_start_end(list_items, start_char, end_char):
        '''
            Pass in a list, a start and end character. This method then returns a new list with the start and end
            characters added to each list item.
        '''
        return [f'{start_char}{i}{end_char}' for i in list_items]
