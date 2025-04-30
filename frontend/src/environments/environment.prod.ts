export const environment = {
  production: true,
  apiUrl: (window as any)['env']['NG_APP_API_URL'] || ''
};
