/* eslint-disable @typescript-eslint/no-explicit-any */
export {};

declare global {
    interface Window {
        recaptchaVerifier: any,
        verificationId: any,
        multiFactor: any
    }
}