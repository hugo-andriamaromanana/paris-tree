Step 1 : Merge 
- type_emplacement has only one unique values, so it will be dropped
- (We could merge the two features geo_points into one tuple & the two mesurements features into one tuple)
- In fact we can't, because Power BI don't accept tuple type, so it will be useless for now

Step 2 : Fill nulls
- We will rename with comple words "stade_developpement" and fill null with "Inconnu"
- We can drop column numero which has 0 values
- We will fill "complement adress" with empty string "", so if we will need to create a full adress we could with "lieu" + "complement adress"
- (Genre, variete and all information about three)'s null values will be fill with "Inconnu"
- remarquable nan values will be considered as 0 : the three wouldn't be Nan if it was remarquable. They are
- for domanialite there is only one missing values, wich can be replace by other instances with same "lieu"