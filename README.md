# Bulk Invitation

### Steps to run 

1. Clone the project and install deps 

```console
$ pip install -r requirements.txt
```

2. Export the names to a csv file

There is a [sample csv file](https://github.com/cazci/bulk-invitation/blob/main/Invitations.csv) in the code 

Use the same format to export invitation list. This can be easily done via google sheets

The columns are;
* Name - The name of the invitee 
* Gender - Gender of the invitee. This is used to detect the correct cut-off value. Currently accepted values are - `m`, `f`, `b`
* Group - Exported images can be grouped by this id 

3. Add the base invitation file to the project root as `invitation.png`

If the file is in `jpeg` or `jpg` formats, modify the filename in [here](https://github.com/cazci/bulk-invitation/blob/2c82116123d106d97d1bc7f2f7ef353e1804b467/transpiler.py#L9) accordingly 

4. Caliberate the offsets

The invitation file should have a field to be filled with the name of the invitee, similar to the following screenshot

![Screenshot 2023-03-06 at 14 58 26](https://user-images.githubusercontent.com/32796120/223487664-c02ac43a-6b52-4896-9873-c7547f97dbd4.png)

Update the following offset values to match the above name field

* https://github.com/cazci/bulk-invitation/blob/2c82116123d106d97d1bc7f2f7ef353e1804b467/transpiler.py#L17

* https://github.com/cazci/bulk-invitation/blob/2c82116123d106d97d1bc7f2f7ef353e1804b467/transpiler.py#L20

* https://github.com/cazci/bulk-invitation/blob/2c82116123d106d97d1bc7f2f7ef353e1804b467/transpiler.py#L23

* https://github.com/cazci/bulk-invitation/blob/2c82116123d106d97d1bc7f2f7ef353e1804b467/transpiler.py#L25

This can be easily done by adding a random value and then slowly moving it to the correct coordinates
