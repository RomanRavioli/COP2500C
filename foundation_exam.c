/**
 * @brief Frees the memory allocated for a smart_string struct.
 * 
 * @param s A pointer to the smart_string struct to be erased.
 * @return smart_string* Returns NULL.
 */
smart_string *erase_smart_string(smart_string *s) {
    if (s == NULL) { // check if the pointer is NULL
        free(s->word); // free the memory allocated for the string
        free(s); // free the memory allocated for the struct
    }
    return NULL;
}

/**
 * @brief Creates a new smart_string struct from an existing one.
 * 
 * @param string A pointer to the smart_string struct to be copied.
 * @return smart_string* Returns a pointer to the new smart_string struct.
 */
smart_string *create_smart_string_from_smart_string(smart_string *string) {
    smart_string *new_string = malloc(sizeof(smart_string));
    new_string->word = string->word;
    new_string->length = string->length;
    return new_string;
}

/**
 * @brief Frees the memory allocated for a smart_string struct.
 * 
 * @param s A pointer to the smart_string struct to be erased.
 * @return smart_string* Returns NULL if the pointer is NULL, otherwise returns the pointer to the struct.
 */
smart_string *erase_smart_string(smart_string *s)
{
    if (s == NULL)
    { // check if the pointer is NULL
        return NULL;
    }
    else
    {
        free(s->word); // free the memory allocated for the string
        free(s);       // free the memory allocated for the struct
    }
}

/**
 * @brief Reads app information from a file and stores it in an array of app pointers.
 * 
 * @param fp A pointer to the file containing the app information.
 * @param numApps An integer indicating the number of apps in the file.
 * @return app** Returns a pointer to the array of app pointers.
 */
app **makeAppArray(FILE *fp, int numApps)
{
    app **appArray = malloc(numApps * sizeof(app *)); // allocate memory for the array of app pointers
    char name[20]; // buffer to store the app name
    float price; // variable to store the app price
    int i = 0; // counter for the loop

    while (i < numApps && fscanf(fp, "%19s %f", name, &price) == 2) // read the app information from the file
    {
        app *newApp = malloc(sizeof(app)); // allocate memory for the app struct
        newApp->name = strdup(name); // allocate memory for the app name and copy it
        newApp->price = price; // set the app price
        appArray[i] = newApp; // add the app to the array
        i++; // increment the counter
    }

    return appArray; // return the array of app pointers
}

/**
 * @brief Converts a linked list to a circular linked list.
 * 
 * @param head A pointer to the head of the linked list.
 * @return node* Returns a pointer to the head of the circular linked list.
 */
typedef struct node
{
    int data;
    struct node *next;
} node;

node *convert_to_circular(node *head)
{
    if (head == NULL)
    {
        return NULL;
    }

    node *current = head;
    while (current->next != NULL)
    {
        current = current->next;
    }

    current->next = head;

    return head;
}
