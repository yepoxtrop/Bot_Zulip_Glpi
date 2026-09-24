SELECT REPLACE(delivery_email, '@aciel.co', '')
FROM zerver_userprofile
WHERE email = 'user14@intrachat.aciel.co';
