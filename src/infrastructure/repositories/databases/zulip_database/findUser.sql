SELECT REPLACE(delivery_email, '@domain', '')
FROM zerver_userprofile
WHERE email = 'user14@zulipdomain.domain';
