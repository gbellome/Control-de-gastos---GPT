// src/types/global.t.ds

declare module '*.scss' {
    const content: {[className: string]:string}
    export default content
}