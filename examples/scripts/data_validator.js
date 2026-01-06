/**
 * 数据验证脚本
 * 提供各种数据验证功能
 */

/**
 * 验证邮箱格式
 * @param {string} email - 邮箱地址
 * @returns {boolean} 是否有效
 */
function validateEmail(email) {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(email);
}

/**
 * 验证 URL 格式
 * @param {string} url - URL 地址
 * @returns {boolean} 是否有效
 */
function validateURL(url) {
    try {
        new URL(url);
        return true;
    } catch {
        return false;
    }
}

/**
 * 验证手机号（中国）
 * @param {string} phone - 手机号
 * @returns {boolean} 是否有效
 */
function validatePhone(phone) {
    const phoneRegex = /^1[3-9]\d{9}$/;
    return phoneRegex.test(phone);
}

/**
 * 验证 JSON 格式
 * @param {string} jsonString - JSON 字符串
 * @returns {object} 验证结果
 */
function validateJSON(jsonString) {
    try {
        const parsed = JSON.parse(jsonString);
        return {
            valid: true,
            data: parsed
        };
    } catch (error) {
        return {
            valid: false,
            error: error.message
        };
    }
}

/**
 * 验证数据对象
 * @param {object} data - 要验证的数据
 * @param {object} schema - 验证规则
 * @returns {object} 验证结果
 */
function validateData(data, schema) {
    const errors = [];
    
    for (const [key, rules] of Object.entries(schema)) {
        const value = data[key];
        
        // 必填验证
        if (rules.required && (value === undefined || value === null || value === '')) {
            errors.push(`${key} 是必填字段`);
            continue;
        }
        
        // 类型验证
        if (value !== undefined && rules.type) {
            const actualType = Array.isArray(value) ? 'array' : typeof value;
            if (actualType !== rules.type) {
                errors.push(`${key} 应该是 ${rules.type} 类型，实际是 ${actualType}`);
                continue;
            }
        }
        
        // 自定义验证函数
        if (value !== undefined && rules.validate && typeof rules.validate === 'function') {
            const result = rules.validate(value);
            if (result !== true) {
                errors.push(`${key}: ${result}`);
            }
        }
    }
    
    return {
        valid: errors.length === 0,
        errors: errors
    };
}

// 命令行接口
if (require.main === module) {
    const args = process.argv.slice(2);
    
    if (args.length < 2) {
        console.error('用法: node data_validator.js <type> <value>');
        console.error('类型: email, url, phone, json');
        process.exit(1);
    }
    
    const type = args[0];
    const value = args[1];
    
    let result;
    
    switch (type) {
        case 'email':
            result = validateEmail(value);
            console.log(result ? '有效' : '无效');
            break;
        
        case 'url':
            result = validateURL(value);
            console.log(result ? '有效' : '无效');
            break;
        
        case 'phone':
            result = validatePhone(value);
            console.log(result ? '有效' : '无效');
            break;
        
        case 'json':
            const jsonResult = validateJSON(value);
            if (jsonResult.valid) {
                console.log('有效 JSON');
                console.log(JSON.stringify(jsonResult.data, null, 2));
            } else {
                console.error('无效 JSON:', jsonResult.error);
                process.exit(1);
            }
            break;
        
        default:
            console.error(`未知类型: ${type}`);
            process.exit(1);
    }
}

module.exports = {
    validateEmail,
    validateURL,
    validatePhone,
    validateJSON,
    validateData
};


